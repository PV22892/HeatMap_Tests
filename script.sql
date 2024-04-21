CREATE TABLE RealEstateData (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL, -- Assuming price is in euros (€)
    type VARCHAR(10) CHECK (type IN ('venda', 'arrendar')), -- Assuming type can only be "venda" or "arrendar"
    location VARCHAR(255), -- Assuming location is a string
    coordinates POINT -- Assuming coordinates are stored as a spatial data type
);
