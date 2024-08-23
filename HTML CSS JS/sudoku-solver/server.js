const PORT = 8080;
const express = require('express');
const app = express();
const path = require('path');

//This command is used to serve static files, which are connected, from 'view' folder.
app.use(express.static(path.join(__dirname, 'view')));

app.use('/', (req, res, next)=>{
    //This command is used to send html file which is kept in 'view' folder 
    res.sendFile(path.join(__dirname, 'view', 'index.html'));
});

app.listen(PORT, () => console.log(`server listening on PORT ${PORT}`));