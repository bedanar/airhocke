import { Popover } from "@headlessui/react";
import Header from "../../components/Header";
import MainTables from "../../components/MainTables";
import MainTitle from "../../components/MainTitle";

const Main = () => {
  return (
    <Popover className="relative z-10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 z-10">
        <Header />
        <MainTitle />
        <MainTables />
      </div>
    </Popover>
  );
};

export default Main;
