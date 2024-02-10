const interIIT = require("../models/interIIT");

const getAllitems = async(req, res) => {
    try {
        const myData = await interIIT.find(req.query);
        res.status(200).json( myData );
    } catch (err) {
        res.status(400).json({ error: 'Error: ' + err });
    }
};
const deleteOneItem = async(req, res) => {
    try {
        await interIIT.findByIdAndDelete(req.params.id);
        res.status(200).json({ message: "User deleted" });
    } catch (err) {
        res.status(400).json({ error: 'Error: ' + err });
    }
};

const getByID = async(req, res) => {
    try {
        const find_entry=await interIIT.findById(req.params.id);
        res.status(200).json( find_entry );
    } catch (err) {
        res.status(400).json({ error: 'Error: ' + err });
    }
};

const addOneItem = async(req, res) => {
    const newListEntry = new interIIT(req.body);
    try {
        const savedListEntry = await newListEntry.save();
        res.redirect("/interIIT/add-user");
    } catch (err) {
        res.status(400).json({ error: 'Error: ' + err });
    }
};

const updateByID = async(req, res) => {
    try {
        const updatedListEntry = await interIIT.findByIdAndUpdate(req.params.id, req.body, { new: true });
        res.status(200).json(updatedListEntry );
    } catch (err) {
        res.status(400).json({ error: 'Error: ' + err });
    }
};


module.exports = {getAllitems, deleteOneItem, addOneItem, getByID, updateByID};