
# Waiting for MongoDB to start
sleep 10

# Initialize the replica set
mongo --host mongodb-0.mongodb:27017 --eval 'rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongodb-0.mongodb:27017" },
    { _id: 1, host: "mongodb-1.mongodb:27017" },
    { _id: 2, host: "mongodb-2.mongodb:27017" }
  ]
})'

