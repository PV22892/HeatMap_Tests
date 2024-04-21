var realestatedata = require('../model/MainModel');
const { Sequelize } = require('sequelize');
const controllers = {};

controllers.list = async (req, res) => {
    try {
        const data = await realestatedata.findAll({
            order: [
                ["id", "ASC"],
            ]
        });
        res.json({ success: true, data: data });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
};

/* LISTAR por user ---------------------- */
controllers.listByLocation = async (req, res) => {
    const { location, type } = req.query;
    try {
        const data = await realestatedata.findAll({
            where: {
                [Sequelize.Op.and]: [
                    { location: { [Sequelize.Op.like]: `%${location}%` } }, // Search for location containing the input string
                    { type: type } // Filter by the specified type
                ]
            },
            order: [
                ["id", "ASC"],
            ]
        });
        res.json({ success: true, data: data });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
};

controllers.maxPrice = async (req, res) => {
    const { location, type } = req.query;
    try {
        const maxPrice = await realestatedata.max('price', {
            where: {
                [Sequelize.Op.and]: [
                    { location: { [Sequelize.Op.like]: `%${location}%` } }, // Search for location containing the input string
                    { type: type } // Filter by the specified type
                ]
            }
        });

        const minPrice = await realestatedata.min('price', {
            where: {
                [Sequelize.Op.and]: [
                    { location: { [Sequelize.Op.like]: `%${location}%` } }, // Search for location containing the input string
                    { type: type } // Filter by the specified type
                ]
            }
        });

        res.json({ success: true, maxPrice: maxPrice, minPrice: minPrice });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
};



/* BUSCAR para EDITAR ----------------------------------------------- */
controllers.get = async (req, res) => {
    const { id } = req.params;
    try {
        const data = await realestatedata.findByPk(id);
        res.json({ success: true, data: data });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
};

module.exports = controllers;
