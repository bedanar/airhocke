import { Popover } from "@headlessui/react";
import { MenuIcon } from "@heroicons/react/outline";
import { Link } from "react-router-dom";
import BurgerMenu from "./BurgerMenu";
import styles from "./Header.module.scss";
import logo from "./../../assets/img/ice-hockey.png";

export const menuList = [
  { href: "#", name: "main" },
  { href: "#", name: "races" },
  { href: "#", name: "rating" },
  //   { href: "#", name: "словари" },
];

const classNames = (...classes) => {
  return classes.join(" ");
};

const Header = () => {
  return (
    <Popover className="relative z-10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6">
        <div className="flex justify-between items-center border-gray-100 py-6 md:justify-start md:space-x-10">
          <div className="flex justify-start lg:w-0 lg:flex-1">
            <Link to="not_found">
              <span className="sr-only">Workflow</span>
              <img
                className="ml-2 h-10 sm:h-10"
                style={{ maxWidth: "4rem" }}
                src={logo}
                alt=""
              />
            </Link>
          </div>
          <div className="-mr-2 -my-2 md:hidden">
            <Popover.Button
              className={classNames(
                "bg-indigo-600 rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:text-gray-500 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500",
                styles.BurgerMenu
              )}
            >
              <span className="sr-only">Open menu</span>
              <MenuIcon className="h-6 w-6" aria-hidden="true" />
            </Popover.Button>
          </div>
          <Popover.Group as="nav" className="hidden md:flex space-x-10">
            {menuList.map((el) => (
              <Link
                key={el.name}
                to={el.href}
                className="text-base font-normal text-md text-white  hover:text-gray-500 mono_text"
              >
                {el.name}
              </Link>
            ))}
          </Popover.Group>
          <div className="hidden md:flex items-center justify-end md:flex-1 lg:w-0">
            <Link
              to="#"
              className={classNames(
                "whitespace-nowrap inline-flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-base font-medium text-white",
                styles.SignInButton
              )}
            >
              Sign in
            </Link>
            <Link
              to="#"
              className={classNames(
                "ml-8 whitespace-nowrap inline-flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-base font-medium text-white",
                styles.SignUpButton
              )}
            >
              Sign up
            </Link>
          </div>
        </div>
      </div>
      <BurgerMenu />
    </Popover>
  );
};

export default Header;
