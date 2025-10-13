import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import heartIcon from './assets/icons/heart.png'
import candyIcon from './assets/icons/candy.png'
import bedIcon from './assets/icons/bed.png'
import base from './assets/sprites/base.png'
import sprite1 from './assets/sprites/0.png'
import sprite2 from './assets/sprites/1.png'
import sprite3 from './assets/sprites/2.png'
import sprite4 from './assets/sprites/3.png'

function StatButton({ icon, statName, onClick}) {
  return (<button
  onClick={() => onClick(statName, 10)}
  className="w-[110px] h-[110px] p-[13px] flex items-center justify-center bg-transparent rounded-[25px] box-border">
    <img src={icon} className="w-[50px] h-[50px]"></img></button>)
}

function StatBar({ icon, value }) {
  const barWidth = 307;
  const fillWidth = (value / 100) * barWidth;

  let color;
  if (value >= 70) color = "#6AD871";
  else if (value >= 40) color = "#FBE044";
  else color = "#F38462";

  return (
    <div id="mood_bar" className="w-[412px] h-[55px] flex flex-row items-center gap-[10px] justify-center px-[30px] py-[5px]">
      <img src={icon} alt="icon" className="w-[35px] h-[35px]" />
      <div
        id="bar_frame" className="relative w-[307px] h-[35px] rounded-[30px] bg-white border-gray-200 box-border"
      >
        <div
          className="h-full rounded-full transition-all duration-50"
          style={{ width: `${fillWidth}px`, backgroundColor: color }}
        />
      </div>
    </div>
  );
}


function App() {
// functions

    // base stats
  const [stats, setStats] = useState({
    love: 70,
    hunger: 50,
    energy: 15 
  });

  const total = stats.hunger + stats.love + stats.energy;
  const average = total / 3;

    //update stats 
  const updateStat = (name, change) => {
    setStats(prev => ({
      ...prev,
      [name]:Math.min(100, Math.max(0, prev[name] + change)),
    }));
  };

  // decay stat
useEffect(() => {
  const interval = setInterval(() => {
    const randomDecay = Math.floor(Math.random() * 3) + 1;

    setStats(prev => ({
      love: Math.max(0, prev.love - randomDecay),
      hunger: Math.max(0, prev.hunger - randomDecay),
      energy: Math.max(0, prev.energy - randomDecay)
    }));
  }, 200000); // every 5 seconds

  return () => clearInterval(interval);
}, []);

  // TODO: DEATH FUNCTION


    // update sprite
  let sprite;
  if(average >= 90) sprite = sprite1;
  else if(average >= 60) sprite = sprite2;
  else if(average >= 40) sprite = sprite3;
  else sprite = sprite4;


  // visuals 
  return (
      <div className="w-screen h-screen relative flex items-center justify-center">
        <div id="home" className="w-[412px] h-[917px] flex flex-col items-center justify-start bg-gradient-to-b from-[#CBA9FF] to-[#8CB4FF]">
          <div id="main" className="w-full flex flex-col items-center justify-start">
          {/* stats 
          TODO: WHITE BACKGROUND*/}
        <div id = "bar-holder" className="w-[412px] h-[180px] flex flex-col items-center justify-center mt-[20px] bg-white">
        <StatBar icon={heartIcon} value={stats.love} />
        <StatBar icon={candyIcon} value={stats.hunger} />
        <StatBar icon={bedIcon} value={stats.energy} />
      </div>
        {/* sprite 
        TODO: FIX SPACING*/}
        <div id="character-frame" className="w-[412px] h-[597px]">
          <div id="holding-frame" className="w-[412px] h-[597px] relative">
            <img 
    src={base} 
    className="h-[588px] absolute bottom-0 left-1/2 transform -translate-x-1/2"></img>
            <img 
  src={sprite} 
  className="h-[588px] absolute bottom-0 left-1/2 transform -translate-x-1/2 z-10" />
          </div>
        </div>


        {/*buttons
        TODO: WHITE BACKGROUND*/}
        <div id="button-frame" className="w-[412px] h-[140px] px-[25px] py-[15px] flex flex-col items-center justify-center bg-white">
          <div id="button-rows" className="w-[362px] h-[110px] justify-center items-center flex flex-row gap-[10px]">
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
