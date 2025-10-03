import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [selected1, setSelected1] = useState("#ffffff");
  const [selected2, setSelected2] = useState("#ffffff");
  const [selected3, setSelected3] = useState("#ffffff");

  const colorOptions = [
    "#ef3d3dff", // Red

"#3b3beaff", // Blue

"#f6f642ff", // Yellow

"#3cf33cff", // Green

"#ef57efff", // Pink

"#808080", // Gray

"#262626ff", // Black

"#ffffff", // White
    ];

const handleDragStart = (e, color) => {
  e.dataTransfer.setData("color", color);
};

const handleDropOn1 = (e) => {
  e.preventDefault();
  const color = e.dataTransfer.getData("color");
  setSelected1(color);
};

const handleDropOn2 = (e) => {
  e.preventDefault();
  const color = e.dataTransfer.getData("color");
  setSelected2(color);
};

const handleDropOn3 = (e) => {
  e.preventDefault();
  const color = e.dataTransfer.getData("color");
  setSelected3(color);
};

const allowDrop = (e) => {
  e.preventDefault();
};



  return (
    <div className="flex flex-col items-center p-6 bg-gray-100 rounded-lg min-h screen">
      <h1 className="text-3xl font-extrabold mb-8 text-indigo-700"> Color Moodboard </h1>

      {/* color palette section */}
      <div className="flex flex-col md:flex-row w-full gap-5">
        <div className="w-full md:w-1/3 bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold mb-4 text-center">
          Color palette
        </h2>
        <p className="mb-4 text-sm text-gray-600">
          Drag Colors to the Boxes
        </p>

        <div className="grid grid-cols-2 gap-2">
          {colorOptions.map((color) => (
            <div 
              key={color}
            className="w-12 h-12 rounded-md shadow-sm cursor-move flex items-center justify-center"
            style={{backgroundColor: color, border: "1px solid #ddd"}}
            draggable="true"
            onDragStart={(e) => handleDragStart(e, color)}>
              {color === "#ef3d3dff" && (
                <span className="text-xs text-white-400">Red</span>
              )}
              {color === "#3b3beaff" && (
                <span className="text-xs text-white-400">Blue</span>
              )}
              {color === "#f6f642ff" && (
                <span className="text-xs text-gray-500">Yellow</span>
              )}
              {color === "#3cf33cff" && (
                <span className="text-xs text-white-400">Green</span>
              )}
              {color === "#ef57efff" && (
                <span className="text-xs text-white-400">Pink</span>
              )}
              {color === "#808080" && (
                <span className="text-xs text-white-400">Grey</span>
              )}
              {color === "#262626ff" && (
                <span className="text-xs text-gray-400">Black</span>
              )}
              {color === "#ffffff" && (
                <span className="text-xs text-gray-400">White</span>
              )}
          </div>
          ))}
        </div>
        </div>
        
        {/*outfit visualization section */}
        <div className="w-full md:w-2/3 bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold mb-4 text-center">Outfit Preview</h2>
        <div classname="flex flex-col items-center">
          <div className="relative w-full h-full flex flex-col items-center justify-center gap-2">
            {/*top section*/}
            <div
              className="w-20 h-20 flex items-center justify-center rounded-md"
              style={{backgroundColor: selected1, border: "1px solid #ddd"}}
              onDrop={handleDropOn1}
              onDragOver={allowDrop}>
                {/* t-shirt */}
              </div>
              <div
              className="w-20 h-20 flex items-center justify-center rounded-md"
              style={{backgroundColor: selected2, border: "1px solid #ddd"}}
              onDrop={handleDropOn2}
              onDragOver={allowDrop}
            >
            </div>
            <div
              className="w-20 h-20 flex items-center justify-center rounded-md"
              style={{backgroundColor: selected3, border: "1px solid #ddd"}}
              onDrop={handleDropOn3}
              onDragOver={allowDrop}
            >
            </div>
          </div>
        </div>
        </div>
        

      



      </div>
  </div>
  )
}

export default App
