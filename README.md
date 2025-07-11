# Schedule Discord Bot

This Discord bot is designed to scan a PDF of UKDW university schedule, extract the schedule data, store it in a MongoDB database, and display a user's schedule in Discord. The main goal is to help users keep track of their classes and get reminders before a class starts.

-----

## Key Features

  * **PDF Schedule Parsing**: Upload and scan a PDF of your college schedule.
  * **MongoDB Integration**: Stores the extracted schedule data in a MongoDB database.
  * **Personalized Schedules**: Each user can have their own schedule stored in the database.
  * **Discord Commands**:
      * `.krs`: Upload your schedule (in PDF format) to be stored in the database.
      * `.kelas`: View your personalized schedule within Discord.
      * `.soal`: Get a random statistics problem.

-----

## Future Vision

The `.statistics` command was created with the vision of expanding the bot into a learning tool. The idea is for the bot to generate questions for students to answer as a quiz, not just for statistics but for other subjects as well. This would require significant development to implement fully.

-----

## Demo

### Usage

\<img src="[https://raw.githubusercontent.com/SanjayaCF/schedule-bot/main/illustration/testing.gif](https://www.google.com/search?q=https://raw.githubusercontent.com/SanjayaCF/schedule-bot/main/illustration/testing.gif)" width="50%"\>

### PDF Schedule Example

\<img src="[https://raw.githubusercontent.com/SanjayaCF/schedule-bot/main/illustration/krs\_example.png](https://www.google.com/search?q=https://raw.githubusercontent.com/SanjayaCF/schedule-bot/main/illustration/krs_example.png)" width="50%"\>

-----

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

  * Python 3.x
  * A Discord Bot application created on the [Discord Developer Portal](https://discord.com/developers/applications)
  * A MongoDB cluster

### Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/SanjayaCF/schedule-bot.git
    cd schedule-bot
    ```

2.  **Create and configure your `.env` file:**

    Create a file named `.env` in the root of the project and add the following, replacing the placeholder values with your actual credentials:

    ```env
    DISCORD_TOKEN=your-discord-bot-token
    MONGO_URI=your-mongodb-client-uri
    DB_CLUSTER=your-cluster-name
    DB_COLLECTION=your-collection-name
    ```

3.  **Run the bot:**

    ```bash
    python main.py
    ```

-----

## Usage

Once the bot is running in your Discord server, you can use the following commands:

  * `.krs`: Upload your KRS PDF to store your schedule.
  * `.kelas`: Display your schedule from the database.

**Note**: You must have your bot invited to your Discord server with the appropriate permissions.

-----

## Project Status

This project is not currently in active development, but I may return to it in the future. Pull requests for new features and improvements are welcome.

-----

## Contributing

Contributions are welcome\! If you'd like to contribute to this project, please feel free to fork the repository and submit a pull request.
