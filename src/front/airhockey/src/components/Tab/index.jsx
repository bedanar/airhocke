import React, {useState} from "react";
import styles from './Tab.module.scss';
import image from '../../assets/img/image.png'

const data = 
    {
        image: image,
        rating: 1,
        username: 'dweebishqys',
        stars: 5,
        gamesAll: 1234,
        gamesWon: 1000,
        gamesLost: 234,
        gamesInfo: [
            {
                id: 1,
                number: 12345,
                date: '30.07.2022',
                opponent: 'desalotAge',
                score: '3:4',
                winner: 'dweebishqys'
            },
            {
                id: 2,
                number: 12345,
                date: '30.07.2022',
                opponent: 'desalotAge',
                score: '3:4',
                winner: 'dweebishqys'
            },
            {
                id: 3,
                number: 12345,
                date: '30.07.2022',
                opponent: 'desalotAge',
                score: '3:4',
                winner: 'dweebishqys'
            },
            {
                id: 4,
                number: 12345,
                date: '30.07.2022',
                opponent: 'desalotAge',
                score: '3:4',
                winner: 'dweebishqys'
            },
            {
              id: 5,
              number: 12345,
              date: '30.07.2022',
              opponent: 'desalotAge',
              score: '3:4',
              winner: 'desalotAge'
          },
        ]
    }



const TabItemContent = ({games}) => {
  return (
    <div className={styles.games}>
    {
      games.map((game, ind) => {
        return <GameInfo key={ind} 
        id={ind} 
        number={game.number}
        date={game.date} 
        opponent={game.opponent}
        score={game.score}
        winner={game.winner} />
      })
    }
  </div>
  )
}
const gamesWon = data.gamesInfo.filter(game => game.winner === data.username)
const gamesLost = data.gamesInfo.filter(game => game.winner !== data.username)
const tabItems = [
  {
    id: 1,
    text: 'all games',
    content: <TabItemContent games={data.gamesInfo} />,
  },
  {
    id: 2,
    text: 'wins',
    content: <TabItemContent games={gamesWon} />,
  },
  {
    id: 3,
    text: 'failures',
    content: <TabItemContent games={gamesLost} />,
  },
];

export function Tab() {
  const [active, setActive] = useState(1);
  
  return (
    <div className={styles.wrapper}>
      <div className={styles.tabs}>
        {tabItems.map(({ id, text } ) => {
          return <TabItemComponent
          key={text}
          onItemClicked={() => setActive(id)}
          isActive={active === id}
          text={text}
        />
        }
      )}
      </div>
      <div className={styles.content}>
        {tabItems.map(({ id, content }) => {
          return active === id ? <div key={id}>{content}</div> : ''
        })}
      </div>
     </div>
  )
}

const TabItemComponent = ({
  text = '',
  onItemClicked = () => console.error('You passed no action to the component'),
  isActive = false,
}) => {
  return (
    <div className={isActive ? styles.tabitem : styles.tabitem__inactive} onClick={onItemClicked}>
      <p className="tabitem__title">{text}</p>
    </div>
  )
};


const GameInfo = ({id, number, date, opponent, score, winner}) => {
    return (
        <div className={styles.game}>
            <p className={styles.game__number}>game №{number}</p>
            <span className="">date: {date}</span>
            <span className="">opponent: @{opponent}</span>
            <span className="">score: {score}</span>
            <span>winner: <p className={winner === opponent ? styles.game__blue : styles.game__pink}>@{winner}</p></span>
        </div>
    )
}