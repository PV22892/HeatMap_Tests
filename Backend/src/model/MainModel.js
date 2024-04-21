const Sequelize = require('sequelize');
const sequelize = require('./database');

const realestatedata = sequelize.define('realestatedata', {
    id: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true,
        allowNull: false
    },
    name: {
        type: Sequelize.STRING(255),
        allowNull: false
    },
    price: {
        type: Sequelize.DECIMAL(10, 2),
        allowNull: false
    },
    type: {
        type: Sequelize.ENUM('venda', 'arrendar'),
        allowNull: false
    },
    location: {
        type: Sequelize.STRING(255),
        allowNull: true
    },
    coordinates: {
        type: Sequelize.GEOMETRY('POINT'),
        allowNull: true
    }
}, {
    timestamps: false
});

module.exports = realestatedata;
