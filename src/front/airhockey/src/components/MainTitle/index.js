import styles from "./MainTitle.module.scss";

const allSquares = [
  styles.SquareFirst,
  styles.SquareSecond,
  styles.SquareThird,
  styles.SquareFourth,
  styles.SquareFifth,
];

const PlayButton = () => {
  return (
    <div className={styles.ButtonWrapper}>
      <button className={styles.PlayButton}>
        {allSquares.map((sqStyle) => (
          <div key={sqStyle} className={`${styles.Square} ${sqStyle}`}></div>
        ))}
        start game
      </button>
    </div>
  );
};

const MainTitle = () => {
  return (
    <>
      <div className={styles.TitleText}>AIR HOCKEY</div>
      <PlayButton />
    </>
  );
};

export default MainTitle;
