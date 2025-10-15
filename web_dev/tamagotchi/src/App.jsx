import { useState, useEffect } from 'react'
import './App.css'

import heartIcon from './assets/icons/heart_icon.png'
import candyIcon from './assets/icons/feed_icon.png'
import bedIcon from './assets/icons/sleep_icon.png'
import base from './assets/sprites/base.png'
import sprite1 from './assets/sprites/0.png'
import sprite2 from './assets/sprites/1.png'
import sprite3 from './assets/sprites/2.png'
import sprite4 from './assets/sprites/3.png'
import lovesprite from './assets/sprites/spritelove.png'
import sleepsprite from './assets/sprites/spritesleep.png'
import feedsprite from './assets/sprites/spritefeed.png'
import deadsprite from './assets/sprites/spritedead.png'


{/* button component*/}
function StatButton({ icon, statName, onClick }) {
  return (
    <button
      onClick={() => onClick(statName, 10)}
      className="w-[70px] h-[70px] p-[8px] flex items-center justify-center bg-transparent rounded-[15px] border-3 border-[#7c6dddff]"
    >
      <img src={icon} className="w-[45px] h-[45px]" />
    </button>
  )
}

{/* stat display*/}
function StatBar({ icon, value }) {
  const barWidth = 200
  const fillWidth = (value / 100) * barWidth

  let color
  if (value >= 70) color = '#6AD871'
  else if (value >= 40) color = '#FBE044'
  else color = '#F38462'

  return (
    <div
      id="mood_bar"
      className="w-[280px] h-[25px] flex flex-row items-center gap-[6px] justify-center px-[15px] py-[3px]"
    >
      <img src={icon} alt="icon" className="w-[32px] h-[32px]" />
      <div
        id="bar_frame"
        className="relative w-[200px] h-[25px] rounded-[20px] bg-[#f4fbf8ff] border-[#f4fbf8ff] border-3"
      >
        <div
        // fills up the bar
          className="h-full rounded-full transition-all duration-50"
          style={{ width: `${fillWidth}px`, backgroundColor: color }}
        />
      </div>
    </div>
  )
}

function App() {
  // code
  // base stats
  const [stats, setStats] = useState({
    love: 70,
    hunger: 50,
    energy: 15
  })

  const total = stats.hunger + stats.love + stats.energy
  const average = total / 3

  const [currentAction, setCurrentAction] = useState(null)

  const updateStat = (name, change) => {
    setStats(prev => ({
      ...prev,
      [name]: Math.min(100, Math.max(0, prev[name] + change))
    }))

    setCurrentAction(name)
    setTimeout(() => setCurrentAction(null), 2000)
  }

  // stat decay
  useEffect(() => {
    const interval = setInterval(() => {
      const randomDecay = Math.floor(Math.random() * 3) + 1
      setStats(prev => ({
        love: Math.max(0, prev.love - randomDecay),
        hunger: Math.max(0, prev.hunger - randomDecay),
        energy: Math.max(0, prev.energy - randomDecay)
      }))
    }, 200000)
    return () => clearInterval(interval)
  }, [])

  // change sprite
  let sprite
  if (currentAction === 'love') sprite = lovesprite
  else if (currentAction === 'hunger') sprite = feedsprite
  else if (currentAction === 'energy') sprite = sleepsprite
  else {
    if (average >= 90) sprite = sprite1
    else if (average >= 60) sprite = sprite2
    else if (average >= 40) sprite = sprite3
    else if (average == 0) sprite = deadsprite
    else sprite = sprite4
  }

  // visuals
  return (
    <div className="w-screen h-screen relative flex items-center justify-center">
      <div
        id="home"
        className="w-full max-w-[300px] h-[600px] flex flex-col items-center bg-gradient-to-b from-[#EFE5FF] to-[#908CFF] overflow-hidden rounded-2xl"
      >
        <div id="main" className="w-full h-full flex flex-col items-center justify-between">
          {/* stat bars */}
          <div
            id="bar-holder"
            className="w-[300px] h-[100px] mt-[10px] flex flex-col items-center justify-center py-[6px] gap-[6px]"
          >
            <StatBar icon={heartIcon} value={stats.love} />
            <StatBar icon={candyIcon} value={stats.hunger} />
            <StatBar icon={bedIcon} value={stats.energy} />
          </div>

          {/* sprite */}
          <div id="character-frame" className="w-[300px] h-[350px] relative">
            <img
              src={base}
              className="h-[360px] absolute bottom-0 left-1/2 transform -translate-x-1/2"
            />
            <img
              src={sprite}
              className="h-[360px] absolute bottom-0 left-1/2 transform -translate-x-1/2 z-10"
            />
          </div>

          {/* buttons */}
          <div
            id="button-frame"
            className="w-[300px] h-[110px] flex flex-col items-center justify-center bg-[#f4fbf8ff]"
          >
            <div
              id="button-rows"
              className="w-[260px] h-full justify-center items-center flex flex-row gap-[6px]"
            >
              <StatButton icon={heartIcon} statName="love" onClick={updateStat} />
              <StatButton icon={candyIcon} statName="hunger" onClick={updateStat} />
              <StatButton icon={bedIcon} statName="energy" onClick={updateStat} />
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
