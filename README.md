# Schedule Discord Bot

This Discord bot is designed to scan a PDF document specific for UKDW schedule, extract the schedule data, store it in a MongoDB database, and display the schedule when the user types `.kelas` in the chat.

## Features

- **PDF Schedule Parsing**: Uploads and scans a PDF document of your college schedule.
- **MongoDB Integration**: Stores the extracted schedule data in a MongoDB database.
- **Discord Command**: Users can type `.krs` alongside their krs pdf to store their schedule into mongoDB.
- **Discord Command**: Users can type `.kelas` to view their schedule within Discord.

## Requirements

- Python 3
- MongoDB (with a configured cluster)
- Discord Bot (configured on the Discord Developer Portal)
- Dependencies (installed via `pip`)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Configure Environment Variables
Create a .env file in the root of your project and add the following:
```env
DISCORD_TOKEN=your-discord-bot-token
MONGO_URI=your-mongodb-client-uri
DB_CLUSTER=your-cluster-name
DB_COLLECTION=your-collection-name
```

### 3.  Running the Bot
After setting up your .env file with the correct credentials, you can run the bot using:
```bash
python main.py
```

### 4. Using the Bot
Once the bot is up and running, use the following command in your Discord server:

`.krs`  : Store schedule into mongoDB based on the krs that are uploaded.
`.kelas`: Displays your schedule from mongoDB.

### Note
- The bot expects the MongoDB URI and database collection to be set up properly in your .env file.
- Ensure you configure your own bot on the [Discord Developer Portal](https://discord.com/developers/applications) and invite it to your server with the appropriate permissions.