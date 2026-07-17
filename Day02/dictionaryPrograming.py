response = {
  "project":"AI Migration",
  "environment":"Production",
  "servers":[
      "web01",
      "web02",
      "db01"
  ]
}
print(response["project"]);
print(response["environment"]);
servers = response["servers"]
for server in servers:
    print("deploying to server: " + server)