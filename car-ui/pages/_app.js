import "bootstrap/dist/css/bootstrap.min.css";
import React from "react";
import { CustomNavBar } from "../components/customNavBar";

function MyApp({ Component, pageProps }) {
  return (
    <>
      <CustomNavBar></CustomNavBar>
      <Component {...pageProps} />
    </>
  );
}

export default MyApp;
