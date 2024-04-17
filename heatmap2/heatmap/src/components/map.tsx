"use client";
import React, { useState } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { Select, SelectItem } from "@nextui-org/react";
import { districts } from "../app/data";
import jsonData from "../app/dummy_data.json";
import L from "leaflet";

// Define the custom green circle icon
const greenIcon = new L.divIcon({
  className: "custom-icon",
  iconSize: [12, 12],
  iconAnchor: [6, 6],
  html: '<div class="green-circle"></div>',
});

// Define CSS for the custom icon
const customIconStyle = `
  .custom-icon {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .green-circle {
    width: 12px;
    height: 12px;
    background-color: green;
    border-radius: 50%;
  }
`;

const Map: React.FC = () => {
  const [selectedValue, setSelectedValue] = useState<string>("");

  const handleChange = (value: string) => {
    setSelectedValue(value);
  };

  const markers = jsonData as MarkerData[];

  const filteredMarkers = selectedValue
    ? markers.filter(
        (marker) => marker.district.toLowerCase() === selectedValue.toLowerCase()
      )
    : [];

  return (
    <div>
      <style>{customIconStyle}</style>

      <Select
        isRequired
        label="Destrito Portugal"
        placeholder="Select an Destrito"
        className="max-w-xs"
        value={selectedValue}
        onChange={(event) => handleChange(event.target.value)}
      >
        {districts.map((district) => (
          <SelectItem key={district.value} value={district.value}>
            {district.label}
          </SelectItem>
        ))}
      </Select>

      <MapContainer
        style={{ height: "calc(100vh - 40px)" }}
        center={[39.3999, -8.2245]}
        zoom={9}
        scrollWheelZoom={true}
        minZoom={9}
        iconDefault={false}
        iconRetina={false}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {filteredMarkers.map((marker) => (
          <Marker
            key={marker.id}
            position={[marker.lat, marker.lng]}
            icon={greenIcon}
          >
            {marker.for_sale && (
              <Popup>
                <div>
                  <p>ID: {marker.id}</p>
                  <p>Price: {marker.price}</p>
                </div>
              </Popup>
            )}
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
};

export default Map;
