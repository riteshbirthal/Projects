import React, { useContext } from 'react';
import { ReactSVG } from 'react-svg';
import './App.css';
import SmartHomeSVG from './smart-home-inverted.svg'; // Adjust the path as necessary
import { GlobalStateContext, GlobalStateProvider } from './GlobalStateContext';

const AppContent = () => {
  const { state, dispatch } = useContext(GlobalStateContext);

  // Fetch the base URLs from environment variables
  const masterBedroomBaseUrl = process.env.REACT_APP_MB_CTRL_URL;
  const hallUrl = `${process.env.REACT_APP_HALL_CTRL_URL}/open_gate`;

  const endpoints = {
    fan: {
      on: `${masterBedroomBaseUrl}/on_fan`,
      off: `${masterBedroomBaseUrl}/off_fan`,
    },
    light: {
      on: `${masterBedroomBaseUrl}/on_tube`,
      off: `${masterBedroomBaseUrl}/off_tube`,
    },
  };

  const controlEndpoint = async (device, action) => {
    const url = endpoints[device][action];
    console.log(`Requesting ${device} to turn ${action}: ${url}`);

    dispatch({ type: 'SET_LOADING', payload: true });

    try {
      const response = await fetch(url, { mode: 'no-cors' });
      if (response.ok || response.status === 0) {
        if (device === 'fan') dispatch({ type: 'SET_FAN_ON', payload: action === 'on' });
        if (device === 'light') dispatch({ type: 'SET_LIGHT_ON', payload: action === 'on' });
      } else {
        throw new Error(`Network response was not ok. Status: ${response.status}`);
      }
    } catch (error) {
      console.error(`Error controlling ${device}:`, error);
      dispatch({ type: 'SET_STATUS', payload: `Error controlling ${device}. ${error.message}` });
    } finally {
      dispatch({ type: 'SET_LOADING', payload: false });
    }
  };

  const toggleFan = () => {
    controlEndpoint('fan', state.fanOn ? 'off' : 'on');
  };

  const toggleLight = () => {
    controlEndpoint('light', state.lightOn ? 'off' : 'on');
  };

  const openGate = async () => {
    console.log('Requesting gate to open:', hallUrl);
    dispatch({ type: 'SET_LOADING', payload: true });

    try {
      const response = await fetch(hallUrl, { mode: 'no-cors' });
      if (response.ok || response.status === 0) {
        // Gate opened successfully
      } else {
        throw new Error(`Network response was not ok. Status: ${response.status}`);
      }
    } catch (error) {
      console.error('Error opening gate:', error);
      dispatch({ type: 'SET_STATUS', payload: `Error opening gate. ${error.message}` });
    } finally {
      dispatch({ type: 'SET_LOADING', payload: false });
    }
  };

  return (
    <div className="main-container">
      <div className="header-container">
        <div className="text-container">
          <h1>Home</h1>
          <h2>Ara Ara</h2>
        </div>
        <div className="icon-container">
          <ReactSVG src={SmartHomeSVG} />
        </div>
      </div>
      <div className="container">
        <div className={`glass-container ${state.lightOn ? 'glow' : ''}`}>
          <div className="icon">💡</div>
          <h1>Master Bedroom</h1>
          <button onClick={toggleLight} className={state.lightOn ? 'active' : ''}>
            <span className="icon">💡</span>
            {state.lightOn ? 'Turn Off Light' : 'Turn On Light'}
          </button>
        </div>
        <div className={`glass-container ${state.fanOn ? 'glow' : ''}`}>
          <div className="icon">💨</div>
          <h1>Master Bedroom</h1>
          <button onClick={toggleFan} className={state.fanOn ? 'active' : ''}>
            <span className="icon">💨</span>
            {state.fanOn ? 'Turn Off Fan' : 'Turn On Fan'}
          </button>
        </div>
        <div className="glass-container">
          <div className="icon">🚪</div>
          <h1>Hall</h1>
          <button onClick={openGate}>
            <span className="icon">🚪</span>
            Open Gate
          </button>
        </div>
      </div>
      <p id="status">{state.status}</p>
      {state.loading && <div className="loading-indicator">Loading...</div>}
    </div>
  );
};

const App = () => (
  <GlobalStateProvider>
    <AppContent />
  </GlobalStateProvider>
);

export default App;
