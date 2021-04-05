import { shallow } from 'enzyme';
import { CustomNavBar }  from '../../components/customNavBar'

describe("NavBarTests", () => {
  
it("should render hello world", () => {


  const html = CustomNavBar()


    const wrapper = shallow(html).toJSON();


    expect(wrapper.text()).toBeTruthy


});

});