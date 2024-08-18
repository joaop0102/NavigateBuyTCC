import React, { useState, useEffect } from 'react';
import axios, { AxiosError } from 'axios';
import { poppins } from "../app/fonts";
import "../components/header.css";
import "../app/globals.css";
import Navbar from "../components/navbar";
import Footer from '@/components/footer';
import Head from 'next/head';

const Editar: React.FC = () => {
  const [username, setUsername] = useState<string>('');
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');

  useEffect(() => {
    // Recupera dados armazenados localmente, se existirem
    const storedEmail = localStorage.getItem('userEmail');
    const storedPassword = localStorage.getItem('userPassword');

    if (storedEmail) setEmail(storedEmail);
    if (storedPassword) setPassword(storedPassword);

    // Remove os dados do localStorage após recuperá-los
    localStorage.removeItem('userEmail');
    localStorage.removeItem('userPassword');

    // Função para buscar dados do usuário
    const fetchUserData = async () => {
      try {
        const response = await axios.get('http://localhost:5001/api/perfil', { withCredentials: true });
        setEmail(response.data.email || '');
        setUsername(response.data.username || '');
      } catch (error) {
        console.error('Erro ao buscar dados do usuário:', error);
      }
    };

    fetchUserData();
  }, []);

  const handleEditProfile = async () => {
    const profileUpdateData = { username, email, password };
    
    try {
      const response = await axios.post('http://localhost:5001/api/perfil', profileUpdateData, { withCredentials: true });
      console.log('Perfil atualizado com sucesso:', response.data);
      alert('Perfil atualizado com sucesso!');
    } catch (error) {
      if (axios.isAxiosError(error)) {
        console.error('Erro ao atualizar perfil:', error.response?.data);
        alert(error.response?.data?.error || 'Erro ao atualizar perfil');
      } else {
        console.error('Erro desconhecido ao atualizar perfil:', error);
        alert('Erro desconhecido ao atualizar perfil');
      }
    }
  };

  const handleLogout = async () => {
    try {
      await axios.post('http://localhost:5001/api/logout', {}, { withCredentials: true });
      alert('Deslogado com sucesso');
      window.location.href = '/login';
    } catch (error) {
      if (axios.isAxiosError(error)) {
        alert(error.response?.data?.message || 'Erro ao fazer logout');
      } else {
        alert('Erro desconhecido ao fazer logout');
      }
    }
  };

  return (
    <div className="flex flex-col min-h-screen">
      <Head>
        <title>Navigate Buy</title>
      </Head>
      <Navbar />
      <header className="flex-grow">
        <h2 className={`text-center font-extrabold mt-10 text-3xl sm:text-2xl md:text-3xl ${poppins.className}`}>
          Perfil
        </h2>
        <p className={`text-center mt-2 text-xl sm:text-lg md:text-xl ${poppins.className}`}>
          Olá {username}
        </p>
        <div className="relative mb-8 space-y-6 max-w-md mx-auto px-4">
          <div className="relative flex flex-col mb-6">
            <label htmlFor="nome-completo" className={`mb-2 text-left ${poppins.className}`}>
              Nome completo:
            </label>
            <input
              id="nome-completo"
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="py-3 px-5 pr-12 sm:px-8 md:px-10 text-xl sm:text-lg md:text-xl rounded-2xl w-full border 
              border-black focus:outline-none focus:border-green-700 shadow-md shadow-green-700 hover:shadow-slate-900 transition duration-500 ease-in-out largeInputOnDesktop"
            />
            <img
              src="../img/icon editar.png"
              alt="Editar"
              className="absolute top-1/2 right-4 transform -translate-y-1/2"
            />
          </div>
          <div className="relative flex flex-col mb-6">
            <label htmlFor="email" className={`mb-2 text-left ${poppins.className}`}>
              Email:
            </label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="py-3 px-5 pr-12 sm:px-8 md:px-10 text-xl sm:text-lg md:text-xl rounded-2xl w-full border 
              border-black focus:outline-none focus:border-green-700 shadow-md shadow-green-700 hover:shadow-slate-900 transition duration-500 ease-in-out largeInputOnDesktop"
            />
          </div>
          <div className="relative flex flex-col mb-6">
            <label htmlFor="senha" className={`mb-2 text-left ${poppins.className}`}>
              Nova Senha:
            </label>
            <input
              id="senha"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="py-3 px-5 pr-12 sm:px-8 md:px-10 text-xl sm:text-lg md:text-xl rounded-2xl w-full border 
              border-black focus:outline-none focus:border-green-700 shadow-md shadow-green-700 hover:shadow-slate-900 transition duration-500 ease-in-out largeInputOnDesktop"
            />
            <img
              src="../img/icon editar.png"
              alt="Editar"
              className="absolute top-1/2 right-4 transform -translate-y-1/2"
            />
          </div>
          <div className="text-center space-x-6 sm:space-x-4">
            <button
              type='button'
              className="mt-6 py-4 px-8 sm:py-2 sm:px-11 text-xl sm:text-base rounded-full border-2
              bg-slate-900 text-white font-semibold transition duration-1000 ease-in-out hover:bg-transparent hover:text-slate-900 hover:border-slate-900"
              onClick={handleEditProfile}
            >
              Editar
            </button>

            <button
              type='button'
              className="mt-6 mb-10 py-3 px-8 sm:py-2 sm:px-8 text-xl sm:text-base rounded-full border-2 
              bg-transparent border-slate-900 shadow-md shadow-slate-900
              text-slate-900 font-semibold transition duration-1000 ease-in-out hover:bg-slate-900 hover:text-white hover:border-slate-900"
              onClick={handleLogout}
            >
              Deslogar
            </button>
          </div>
        </div>
      </header>
      <Footer />
    </div>
  );
};

export default Editar;