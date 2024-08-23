import back1 from "./images/section1_backgrounds/5.jpg";
// import back2 from "./images/section2_backgrounds/3.jpg";
import light_on from "./images/on_bulb.png";
import light_off from "./images/off_bulb.png";
import fan_img from "./images/fan_2.png";
import './App.css';
import { useState } from "react";


function App() {
	const [light, setLight] = useState(false);
	const [fan, setFan] = useState(false);
	const [gate, setGate] = useState(false);

	const light_path = light ? light_on : light_off;
	const light_text = light ? "Turn Off Light" : "Turn On Light";
	const fan_path = fan_img;
	const fan_text = fan ? "Turn Off Fan" : "Turn On Fan";
	const gate_text = gate ? "Gate Opened" : "Open Gate";

	const light_func = () => {
		setLight(!light);
		return;
	};

	const fan_func = () => {
		setFan(!fan);
		return;
	};

	const gate_func = () => {
		setGate(true);
		setTimeout(() => {
			setGate(false);
		}, 1000);
		return;
	};

	const card = (c_name, img_src, button_text, func) => {
		return (
			<>
				<div className="card" style={{ textAlign: 'center', backgroundColor: 'rgba(255, 255, 255, 0.2)', borderRadius: "2vw", padding: "1vw 0" }}>
					<div>
						<img className={c_name} src={img_src} alt="Avatar" style={{ width: "15vw", height: "15vw", borderRadius: "2em" }} />
					</div>
					<div className="container" style={{ width: "100%" }}>
						<button onClick={func} style={{ width: "15vw", fontSize: "1.2vw", borderRadius: "1vw", padding: "0.5vh 1vw", margin: "2em 0em" }}>{button_text}</button>
					</div>
				</div>
			</>
		);
	}
	return (
		<div style={{
			width: "100vw", height: "100vh", backgroundImage: `url(${back1}`,
			backgroundPosition: 'center', backgroundSize: 'cover', backgroundRepeat: 'no-repeat'
		}}>
			<div className="Header-Section" style={{ width: "100vw", height: "40vh", textAlign: 'center' }}>
				<h1 style={{ fontSize: "8em", color: "white" }}> Home Ara-Ara</h1>
			</div>
			<div className="App" style={{ display: 'flex', flexDirection: 'row', height: "25vh" }}>
				<div style={{ width: "25vw", margin: "5vw" }}>
					{card("light_class", light_path, light_text, light_func)}
				</div>
				<div style={{ width: "25vw", margin: "5vw" }}>
					{card(`fan_class ${fan ? 'spinning' : ''}`, fan_path, fan_text, fan_func)}
				</div>
				<div style={{ width: "25vw", margin: "5vw" }}>
					<div className="card" style={{ textAlign: 'center', backgroundColor: 'rgba(255, 255, 255, 0.2)', borderRadius: "2vw", padding: "1vw 0" }}>
						<div style={{textAlign: 'center', alignItems: 'center', justifyContent: 'center', display:'flex'}}>
							<div className="flipbox">
								<div className={`flipbox-active ${gate ? 'gate-opened' : ''}`}>
								</div>
							</div>
						</div>
						<div className="container" style={{ width: "100%" }}>
							<button onClick={gate_func} style={{ width: "15vw", fontSize: "1.2vw", borderRadius: "1vw", padding: "0.5vh 1vw", margin: "2em 0em" }}>{gate_text}</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	);
}

export default App;
