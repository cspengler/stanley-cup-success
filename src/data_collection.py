import requests
import json
import time
import os
from typing import Dict, Optional, Any
import logging

"""
Class to manage retrieving data from the NHL API. Necessary capabilites:
- general function to execute get requests, with failsafes for timeouts or access errors
- functions to query for specific data required: team rosters, nationalities, playoff finish, year, etc.
"""
class HockeyDataCollector:
	# specify main url for NHL API
	base_url = "https://api-web.nhle.com/v1/"

	"""
	initialize data collector
	
	args:
		rate_limit: Maximum API calls per second
		data_dir: Directory to save raw data files
	"""
	def __init__(self, rate_limit: float = 1.0, data_dir: str = 'data/raw'):

        self.rate_limit = rate_limit
        self.data_dir = data_dir
        self.last_request_time = 0
        
        # make sure data directory exists, create if needed
        os.makedirs(data_dir, exist_ok=True)

	def _rate_limited_request(self, url: str, max_retries: int = 3) -> Optional[Dict[Any, Any]]:
        """
        Make rate-limited API request with error handling
        
        Args:
            url: API endpoint URL
            max_retries: Maximum number of retry attempts
            
        Returns:
            JSON response data or None if failed
        """
        # calculate request rate
        time_since_last = time.time() - self.last_request_time
        min_interval = 1.0 / self.rate_limit
        if time_since_last < min_interval:
            sleep_time = min_interval - time_since_last
            time.sleep(sleep_time)
        
        for attempt in range(max_retries):
            try:
                logger.info(f"Making request to: {url}")
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                
                self.last_request_time = time.time()
                return response.json()
                
            except requests.exceptions.HTTPError as e:
                logger.error(f"HTTP error on attempt {attempt + 1}: {e}")
                if response.status_code == 429:  # Rate limit exceeded
                    sleep_time = 2 ** attempt
                    logger.info(f"Rate limited. Sleeping for {sleep_time} seconds.")
                    time.sleep(sleep_time)
                elif response.status_code >= 500:  # Server error
                    time.sleep(2 ** attempt)
                else:
                    break
                    
            except requests.exceptions.RequestException as e:
                logger.error(f"Request error on attempt {attempt + 1}: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                    
            except ValueError as e:
                logger.error(f"JSON parsing error: {e}")
                break
        
        logger.error(f"Failed to fetch data from {url} after {max_retries} attempts")
        return None
