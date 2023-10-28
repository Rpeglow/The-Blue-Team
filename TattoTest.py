# FILEPATH: /c:/Users/peglo/OneDrive/Desktop/The Blue Team/TattoTest/main.py

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Client(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.design_requests = []

    def request_design(self, artist, design):
        artist.receive_request(self, design)

class Artist(User):
    def __init__(self, username, password, tags):
        super().__init__(username, password)
        self.tags = tags
        self.portfolio = []
        self.awards = []

    def add_to_portfolio(self, design):
        self.portfolio.append(design)

    def receive_request(self, client, design):
        # send notification to artist
        pass

class SocialMediaPlatform:
    def __init__(self):
        self.clients = []
        self.artists = []

    def register_client(self, username, password):
        self.clients.append(Client(username, password))

    def register_artist(self, username, password, tags):
        self.artists.append(Artist(username, password, tags))

    def search_artists_by_tag(self, tag):
        return [artist for artist in self.artists if tag in artist.tags]

# Example usage
platform = SocialMediaPlatform()

# Register clients
platform.register_client("client1", "password1")
platform.register_client("client2", "password2")

# Register artists
platform.register_artist("artist1", "password1", ["traditional", "blackwork"])
platform.register_artist("artist2", "password2", ["realism", "watercolor"])

# Search for artists by tag
artists = platform.search_artists_by_tag("traditional")
print([artist.username for artist in artists])

# Request a design
client = platform.clients[0]
artist = platform.artists[0]
client.request_design(artist, "dragon tattoo design")
