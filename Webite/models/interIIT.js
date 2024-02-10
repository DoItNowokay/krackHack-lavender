const mongoose = require("mongoose");

const interIITModel = new mongoose.Schema({
    edition: {
        type: Number,
        required: [true, "Edition must be provided"],
    },
    medal: {
        type: String,
        required: true,
    },
    ps: {
        type: String,
        required: true,
    },
    team: {
        type: String,
        required: true,
    },
    usertype: {
        type: String,
        required: true,
    }
});

module.exports = mongoose.model("interIITModel", interIITModel)