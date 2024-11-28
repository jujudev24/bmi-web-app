import React, { useState } from "react";  
import "./App.css";

function App() {
  const [weight, setWeight] = useState("");
  const [height, setHeight] = useState("");
  const [bmi, setBMI] = useState(null);
  const [category, setCategory] = useState("");

  const calculateBMI = () => {
    if (weight <= 0 || height <= 0) {
      alert("Please enter valid positive numbers for weight and height!");
      return;
    }
    
    if (weight && height) {
      const heightInMeters = height > 10 ? height / 100 : height; // Convert to meters
      const bmiValue = (weight / (heightInMeters * heightInMeters)).toFixed(2);
      setBMI(bmiValue);
  
      let bmiCategory = "";
      if (bmiValue < 18.5) bmiCategory = "Underweight";
      else if (bmiValue < 24.9) bmiCategory = "Normal weight";
      else if (bmiValue < 29.9) bmiCategory = "Overweight";
      else bmiCategory = "Obesity";
  
      setCategory(bmiCategory);
    } else {
      alert("Please enter both weight and height!");
    }
  };
  

  return (
    <div className="App">
      <div className="card">
        <h1 className="title">BMI Calculator</h1>
        <div className="bmi-form">
          <label>Weight (kg):</label>
          <input
            type="number"
            value={weight}
            onChange={(e) => setWeight(e.target.value)}
            placeholder="Enter your weight"
          />
          <label>Height (m):</label>
          <input
            type="number"
            step="0.01"
            value={height}
            onChange={(e) => setHeight(e.target.value)}
            placeholder="Enter your height"
          />
          <button onClick={calculateBMI}>Calculate BMI</button>
        </div>
        {bmi && (
          <div className="bmi-result">
            <h2>Your BMI: {bmi}</h2>
            <h3>Category: {category}</h3>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
