var Sequelize = require('sequelize');
const sequelize = new Sequelize(
    'postgres', // bd name
    'postgres', // username
    'password', // password
    {
        host: 'database',
        port: '5432',
        dialect: 'postgres'
    }
);

module.exports = sequelize;
