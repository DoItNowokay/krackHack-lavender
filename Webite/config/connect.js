const mongoose = require("mongoose");
require("dotenv").config({path:"config/.env"})

const connectDB = async () => {
    try {
         const Database = process.env.DATABASE_URI.replace(
             "<password>",
             process.env.DATABASE_PASSWORD
         );
        mongoose
            .connect(Database, {
                useNewUrlParser: true,
                useUnifiedTopology: true,
            })
            .then(() => console.log("DB connection successful!"));
    } catch (err) {
        console.error(err);
        process.exit(1);
    }
};

module.exports = connectDB;