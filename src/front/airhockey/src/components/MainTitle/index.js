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
          <div className={`${styles.Square} ${sqStyle}`}></div>
        ))}
        start game
      </button>
    </div>
  );
};

const MainTitle = () => {
  return (
    <div className="relative z-10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 z-10">
        <div className={styles.TitleText}>AIR HOCKEY</div>
        <PlayButton />
      </div>
    </div>
  );
};

export default MainTitle;
