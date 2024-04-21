CREATE TABLE RealEstateData (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    type VARCHAR(10) CHECK (type IN ('venda', 'arrendar')),
    location VARCHAR(255),
    coordinates POINT
);
