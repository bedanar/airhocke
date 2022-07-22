import styles from "./BlurBall.module.scss";

const Ball = ({ color, is_up }) => {
  const PERCENT_OUT = 70;
  const CLIMB_OUT_STYLES = is_up
    ? { top: `-${PERCENT_OUT}vh`, left: `-${PERCENT_OUT}vw` }
    : { bottom: `-${PERCENT_OUT}vh`, right: `-${PERCENT_OUT}vw` };

  return (
    <div
      className={styles.Ball}
      style={{
        backgroundImage: `radial-gradient(${color}, transparent)`,
        ...CLIMB_OUT_STYLES,
      }}
    ></div>
  );
};

const BlurBallsBack = (props) => {
  return (
    <div className={styles.Back}>
      <Ball color="#001FC2" is_up={false} />
      {props.children}
      <Ball color="#C20046" is_up={true} />
    </div>
  );
};

export default BlurBallsBack;
