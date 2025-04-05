import requests


class DatsCityClient:
    """Client for interacting with the DatsCity API."""

    def __init__(
            self,
            base_url: str = "https://games-test.datsteam.dev",
            token: str = "a4ecfa3b-fd40-440e-b585-9400d4c50ad0",
    ):
        """Initialize the DatsCity API client.

        Args:
            base_url: The base URL of the DatsCity API.
        """
        self.base_url = base_url
        self.api_path = "/api"
        self.session = requests.Session()
        self.token = token

    def _get_url(self, endpoint: str) -> str:
        """Construct the full URL for the given endpoint."""
        return f"{self.base_url}{self.api_path}{endpoint}"

    def _get_headers(self) -> dict[str, str]:
        """Get the headers for API requests."""
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["X-Auth-Token"] = f"{self.token}"
        return headers

    def _request(self, method: str, endpoint: str, data: any = None, params: dict = None) -> dict:
        """Make an HTTP request to the API.

        Args:
            method: The HTTP method (GET, POST, PUT, DELETE).
            endpoint: The API endpoint.
            data: The request body data.
            params: The query parameters.

        Returns:
            The response data as a dictionary.
        """
        url = self._get_url(endpoint)
        headers = self._get_headers()

        response = self.session.request(
            method=method,
            url=url,
            headers=headers,
            json=data if data else None,
            params=params
        )

        response.raise_for_status()

        if response.text:
            return response.json()
        return {}

    def get_words(self):
        """Get the words from the API."""
        return self._request("GET", "/words")

    def build(self, done: bool, words):
        data = {"done": done, "words": words}
        return self._request("POST", "/build", data=data)

    def towers(self):
        return self._request("GET", "/towers")

    def rounds(self):
        return self._request("GET", "/rounds")

    def shuffle(self):
        return self._request("GET", "/shuffle")
