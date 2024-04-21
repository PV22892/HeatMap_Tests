const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const mainRouters = require('./routes/MainRoute.js');

const app = express();

// Configurations
app.set('port', process.env.PORT || 8000);

// Middlewares
app.use(express.json());
app.use(cors());
app.use(bodyParser.urlencoded({ extended: true }));

// Routes
// Instead of directly passing the router object, use the router middleware function
app.use('/', mainRouters);

// Start the server
app.listen(app.get('port'), () => {
    console.log("Server started on port " + app.get('port'));
});
