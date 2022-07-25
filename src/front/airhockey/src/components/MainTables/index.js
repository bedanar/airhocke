import Table from "./Table";
import styles from "./MainTables.module.scss";

const firstTable = {
  keys: {
    user: "user",
    score: "points",
    quantity: "number of competitions",
  },
  values: [
    { user: "iamdweebish", score: 12, quantity: 1234 },
    { user: "iamdweebish", score: 12, quantity: 1234 },
    { user: "iamdweebish", score: 12, quantity: 1234 },
    { user: "iamdweebish", score: 12, quantity: 1234 },
  ],
};

const secondTable = {
  keys: {
    user: "user",
    score: "points",
    quantity: "number of competitions",
  },
  values: [
    { user: "iamdweebish", score: 12, quantity: 1234 },
    { user: "iamdweebish", score: 12, quantity: 1234 },
    { user: "iamdweebish", score: 12, quantity: 1234 },
    { user: "iamdweebish", score: 12, quantity: 1234 },
  ],
};

const MainTables = () => {
  return (
    <div className={styles.MainWrapper}>
      <Table title={"rating"} description={firstTable} />
      <Table title={"races"} description={secondTable} />
    </div>
  );
};

export default MainTables;
