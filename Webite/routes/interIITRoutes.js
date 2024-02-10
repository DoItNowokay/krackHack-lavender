const express = require("express");
const route = express.Router();

const services=require("../services/render");

route.get("/",services.homeRoutes); 
route.get("/add-user",services.add_user);
route.get("/update-user",services.update_user);

const { getAllitems, deleteOneItem, addOneItem, getByID, updateByID } = require("../controllers/interIIT_controller");

route.post("/api/addOneItem",addOneItem);
route.get("/api/getAllItems",getAllitems);
route.get("/api/getByID/:id",getByID);
route.put("/api/updateByID/:id",updateByID);
route.delete("/api/deleteOneItem/:id",deleteOneItem);

module.exports = route;