import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import { OwnerShowALL } from './components/owners/OwnersShowAll';
import './index.css'


export const GlobalURL="http://127.0.0.1:8000/";//This may change in AWS;


ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
