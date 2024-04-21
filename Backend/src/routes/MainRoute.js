const express = require('express');
const router = express.Router();
const main = require('../controllers/MainController');

router.get('/list', main.list);
router.get('/listByLocation', main.listByLocation);
router.get('/maxPrice', main.maxPrice);
router.get('/get/:id', main.get);

module.exports = router;
