import React from "react";
import { Container, Table } from "react-bootstrap";
import CarTable from "../components/CarTableComponent";

export default function Data() {
  return (
    <Container>
      <h1>Data</h1>
      <p> This is the data page</p>
      <CarTable></CarTable>
    </Container>
  );
}
