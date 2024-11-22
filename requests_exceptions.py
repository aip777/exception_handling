import requests

# The base class for all exceptions raised by the requests library.
try:
    response = requests.get('https://non_existent_website.com')
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")  # Handles any request-related error


# Raised for HTTP error responses, such as 4xx or 5xx.
try:
    response = requests.get('https://httpbin.org/status/404')
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")  # Output: HTTP error: 404 Client Error: Not Found


# Raised when the connection to the server fails, such as DNS failures, refused connections etc.
try:
    response = requests.get('https://non_existent_domain.com')
except requests.exceptions.ConnectionError as e:
    print(f"Connection error: {e}")  # Output: Connection error


# Raised when a request times out.
try:
    response = requests.get('https://httpbin.org/delay/10', timeout=3)  # Timeout set to 3 seconds
except requests.exceptions.Timeout as e:
    print(f"Timeout error: {e}")  # Output: Timeout error


# Raised when too many redirects occur.
try:
    response = requests.get('https://httpbin.org/redirect/10')  # By default, max redirects is 30
except requests.exceptions.TooManyRedirects as e:
    print(f"Too many redirects: {e}")  # Output: Too many redirects


# Raised when a valid URL is not provided
try:
    response = requests.get('')
except requests.exceptions.URLRequired as e:
    print(f"URL required error: {e}")  # Output: URL required error


# Raised when the missing (http:// or https://)
try:
    response = requests.get('www.example.com')  #
except requests.exceptions.MissingSchema as e:
    print(f"Missing schema error: {e}")

# Raised when the URL has an unsupported or invalid schema
# 'ftp' is not supported
try:
    response = requests.get('ftp://example.com')
except requests.exceptions.InvalidSchema as e:
    print(f"Invalid schema error: {e}")  # Output: Invalid schema error

# Invalid URL format
try:
    response = requests.get('http://[invalid-url]')
except requests.exceptions.InvalidURL as e:
    print(f"Invalid URL error: {e}")  # Output: Invalid URL error

# Raised when there an issue with chunked transfer encoding.
# This can occur when the server closes the connection before sending the complete data
from requests.exceptions import ChunkedEncodingError

try:
    response = requests.get('https://httpbin.org/stream/20')
    raise ChunkedEncodingError("Simulated chunked encoding error")
except ChunkedEncodingError as e:
    print(f"Chunked encoding error: {e}")  # Output: Chunked encoding error



# Raised when the server response is not correctly encoded making it undecodable.
from requests.exceptions import ContentDecodingError

try:
    raise ContentDecodingError("Simulated content decoding error")
except ContentDecodingError as e:
    print(f"Content decoding error: {e}")  # Output: Content decoding error

# Raised when there is an SSL certificate error during the HTTPS request
try:
    response = requests.get('https://self-signed.badssl.com/')
except requests.exceptions.SSLError as e:
    print(f"SSL error: {e}")  # Output: SSL error

# Raised when there is an issue with the headers provided in the request.
try:
    headers = {'Invalid Header': '\nValue'}
    response = requests.get('https://httpbin.org/get', headers=headers)
except requests.exceptions.InvalidHeader as e:
    print(f"Invalid header error: {e}")  # Output: Invalid header error

