import React, { useState } from "react";
import { Container, Table, Form } from "react-bootstrap";
import faker from "faker";
import { BADNAME } from "node:dns";

interface ImageData {
  image: string; // probably base64 encoded
  id: number;
  numCars?: number;
}

interface CarTableProps {
  data: ImageData[];
}

function CarOptions(data: { numCars: number }) {
  const [state, setState] = useState(data.numCars ? data.numCars : 0);

  return (
    <div>
      <Form
        onChange={(value) => {
          // will post an update to server database
          setState(value.target.defaultValue);
        }}
      >
        <Form.Check
          type="radio"
          inline
          label="1"
          value={1}
          checked={state == 1}
        ></Form.Check>
        <Form.Check
          type="radio"
          inline
          label="2"
          value={2}
          checked={state == 2}
        ></Form.Check>
        <Form.Check
          type="radio"
          inline
          label="3"
          value={3}
          checked={state == 3}
        ></Form.Check>
        <Form.Check
          type="radio"
          inline
          label="4"
          value={4}
          checked={state == 4}
        ></Form.Check>
      </Form>
    </div>
  );
}
enum SortBy {
  ID_ASC,
  ID_DES,
  HAS_DATA,
}

export default class CarTable extends React.Component {
  data: ImageData[];
  constructor(props) {
    super(props);
    this.state = {
      sortType: SortBy.HAS_DATA,
    };
    this.data = []
  }
  render() {
    for (let i = 0; i < 20; i++) {
      this.data.push({
        image: faker.image.imageUrl(),
        id: faker.datatype.number(),
        numCars: faker.datatype.number(),
      });
    }
    switch (this.state.sortType) {
      case SortBy.ID_ASC:
        this.data.sort((a, b) => a.id - b.id);
        break;
      case SortBy.ID_DES:
        this.data.sort((a, b) => b.id - a.id);
        break;
      case SortBy.HAS_DATA:
        this.data.sort((a, b) => {
          if (a.numCars && b.numCars) {
            return 0;
          } else if (a.numCars && !b.numCars) {
            return 1;
          } else if (!a.numCars && b.numCars) {
            return -1;
          } else if (!a.numCars && !b.numCars) {
            return 0;
          }
        });
        break;
    }

    return (
      <Container>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>#</th>
              <th>Image</th>
              <th># of Cars</th>
            </tr>
          </thead>
          <tbody>
            {this.data.map((image) => (
              <tr>
                <td>{image.id}</td>
                <td>
                  <img src={image.image}></img>
                </td>
                <td>
                  <CarOptions numCars={image.numCars}></CarOptions>
                </td>
              </tr>
            ))}
          </tbody>
        </Table>
      </Container>
    );
  }
}
