import { shallow } from "enzyme";
import { NextNavLink }  from '../../components/customNavBar'

describe("NavBarTests", () => {
  it("should render hello world", () => {
    const html = NextNavLink({ href: "/", children: "Hello World!" });

    const wrapper = shallow(html).toJSON();

    expect(wrapper.text()).toContain("Hello World!");
  });
});
