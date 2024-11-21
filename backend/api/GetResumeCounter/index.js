// Counter function for Azure Resume Project - Updated deployment
const { CosmosClient } = require("@azure/cosmos");

const config = {
    endpoint: process.env.COSMOS_DB_ENDPOINT,
    key: process.env.COSMOS_DB_KEY,
    databaseId: "CounterDB",
    containerId: "Counter",
    partitionKey: { kind: "Hash", paths: ["/id"] }
};

module.exports = async function (context, req) {
    const client = new CosmosClient({
        endpoint: config.endpoint,
        key: config.key
    });

    const database = client.database(config.databaseId);
    const container = database.container(config.containerId);

    try {
        // Query for the counter document
        const { resources } = await container.items
            .query("SELECT * FROM c WHERE c.id = '1'")
            .fetchAll();

        let counter = resources[0];
        
        // Increment the counter
        counter.count++;

        // Update the document in Cosmos DB
        const { resource: updatedCounter } = await container
            .item(counter.id)
            .replace(counter);

        context.res = {
            body: updatedCounter.count,
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        };
    } catch (error) {
        context.res = {
            status: 500,
            body: "Error updating counter: " + error.message,
            headers: {
                'Access-Control-Allow-Origin': '*'
            }
        };
    }
};
