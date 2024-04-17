import React from "react";
import {Select, SelectItem} from "@nextui-org/react";
import {districts} from "../data";

export default function dropdown() {
  return (
    <Select
      isRequired
      label="Favorite Animal"
      placeholder="Select an animal"
      defaultSelectedKeys={["cat"]}
      className="max-w-xs"
    >
      {animals.map((animal) => (
        <SelectItem key={animal.value} value={animal.value}>
          {animal.label}
        </SelectItem>
      ))}
    </Select>
  );
}
