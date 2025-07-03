## Persistent Storage in ADK

This example demonstrates how to implement persistent storage for your ADK
agents, allowing them to remember information and maintain conversation history across multiple sessions, application restarts, and even server deployments.

## What is Persistent Storage in ADK?

In previous examples, we used `InMemorySessionService` which stores session
data only in memory - this data is lost when the application stops. For real-world applications, you'll often need your agents to remember user information and conversation history long-term. This is where persistent storage comes in.

ADK provides the `DatabaseSessionService` that allows you to store session data in a SQL database, ensuring: 1. Long-term Memory: Information persists across application restarts 2. Consistent User Experiences: Users can continue conversations where they left off 3. Multi-user Support: Different user's remains separate and secure 4. Scalability: Works with production database for high-scale deployments

# Running the Example

To run the persistent storage example, switch to the agent directory and run:

```bash
python main.py
```

This will:

    1. Connect to the SQLite database (or create it if it doesn't exist)
    2. Check for previous sessions for the user
    3. Start a conversation with the memory agent
    4. Save all interactions to the database

# Using Database Storage in Production

While this example uses SQLite for simplicity, `DatabaseSessionService` supports various database backends through SQLAlchemy:

    * PostgreSQL: `postgresql://user:password@localhost/dbname`
    * MySQL: `mysql://user:password@localhost/dbname`
    * MS SQL SERVER: `mssql://user:password@localhost/dbname`
