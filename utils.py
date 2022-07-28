def totalServers(client):
    return len(client.guilds)

def totalUsers(client):
    return sum([server.member_count for server in client.guilds])