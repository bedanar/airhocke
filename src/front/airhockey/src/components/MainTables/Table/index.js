import Pagination from "../../Pagination";
import styles from "./Table.module.scss";

const Table = ({ title, description }) => {
  const order = Object.keys(description.keys);

  const getRaw = (ind) => {
    return (
      <tr>
        {order.map((el) => {
          return <td>{description.values[ind][el]}</td>;
        })}
      </tr>
    );
  };

  return (
    <div className={styles.TableWrapper}>
      <h1 className={styles.Title}> {title}</h1>
      <table className={styles.Table}>
        <thead>
          <tr>
            {order.map((el) => (
              <th key={el}>{description.keys[el]}</th>
            ))}
          </tr>
        </thead>
        <tbody>{description.values.map((_, ind) => getRaw(ind))}</tbody>
      </table>
      <div className={styles.table__pagination}>
        <Pagination numbers={5} color={""} />
      </div>
    </div>
  );
};

export default Table;
