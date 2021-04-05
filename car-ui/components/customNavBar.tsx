import React from "react";
import { Nav, Navbar, NavLink } from "react-bootstrap";
import Link from "next/link";

interface NavLinkProps {
  href: string;
  children: string;
}

export function NextNavLink(props: NavLinkProps) {
  return (
    <Link href={props.href}>
      <Nav.Link as="a" href={props.href}>{props.children}</Nav.Link>
    </Link>
  );
}

export function CustomNavBar() {
  return (
    <Navbar bg="dark" variant="dark">
      <Nav className="mr-auto">
        <NextNavLink href="/">Home</NextNavLink>
        <NextNavLink href="/data">Data</NextNavLink>
        <NextNavLink href="/training">Training</NextNavLink>
      </Nav>
    </Navbar>
  );
}
