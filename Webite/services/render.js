const axios=require("axios");

exports.homeRoutes=(req,res)=>{
    axios.get("http://localhost:9000/interIIT/api/getAllItems")
    .then(function(response){
        res.render('index', { users : response.data });
    })
    .catch(err =>{
        res.send(err);
    })
}

exports.add_user=(req,res)=>{
    res.render("add_user");
}

exports.update_user=(req,res)=>{
    const userId = req.query.id;
    axios.get(`http://localhost:9000/interIIT/api/getByID/${userId}`)
        .then(function(userdata){
            res.render("update_user", { user : userdata.data})
        })
        .catch(err =>{
            res.send(err);
        })
}