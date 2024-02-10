// require("dotenv").config(); 
const express = require("express");
const app = express();
const connectDB = require("./config/connect");
const morgan = require("morgan");
const bodyparser = require("body-parser")
const path = require("path");
const dotenv = require("dotenv");
const cors = require('cors');

app.use(cors());
port = process.env.PORT || 9000;
app.use(morgan(`tiny`));
app.use(bodyparser.urlencoded({ extended: true }));
app.set("view engine", "ejs")
app.set('views', path.join(__dirname, 'views', 'interIITviews'));

const interIIT_routes = require("./routes/interIITRoutes");

app.use("/interIIT", interIIT_routes);
app.use("/css", express.static(path.resolve(__dirname, "assets/CSS")))
app.use("/interIIT/css", express.static(path.resolve(__dirname, "assets/CSS")))
app.use("/js", express.static(path.resolve(__dirname, "assets/js")))


dotenv.config({ path: "./config/config.env" });

const start = async () => {
    try {
        await connectDB(process.env.MONGODB_URL);
        app.listen(port, () => {
            console.log(`${port} Yes I am connected
            http://localhost:9000`);
        });

    } catch (error) {
        console.log(error);
    }
};

start(); 
