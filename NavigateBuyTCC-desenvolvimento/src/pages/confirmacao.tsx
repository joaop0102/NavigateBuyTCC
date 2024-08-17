import React, { useState } from 'react';
import Head from 'next/head';
import { useRouter } from 'next/router'; // Corrigida a importação do useRouter
import "../app/globals.css";

const Confirmacao = () => {
  const [code, setCode] = useState('');
  const [email, setEmail] = useState('');
  const [isEmailSent, setIsEmailSent] = useState(false);
  const router = useRouter();

  const handleSendCode = async (e: React.FormEvent) => {
    e.preventDefault();
  
    try {
      const response = await fetch('http://localhost:5000/api/send_code', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email }),
      });      
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const data = await response.json();
      alert(data.message || 'Código de confirmação enviado!');
      setIsEmailSent(true);
    } catch (error) {
      console.error('Erro ao enviar o código:', error);
      alert('Erro ao enviar o código. Por favor, tente novamente.');
    }
  };
  
  const handleConfirmation = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:5000/api/confirm_code', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email,
          code: code,
        }),
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      router.push('/editar-perfil'); // Redireciona para a página de edição de perfil
    } catch (error) {
      console.error('Erro na confirmação:', error);
    }
  };

  return (
    <>
      <Head>
        <title>Confirmar Código</title>
      </Head>
      <div className="flex flex-col h-screen bg-white">
        <div className="flex-1 flex flex-col items-center justify-center">
          <div className="max-w-md mx-auto p-6 sm:p-8 lg:p-12">
            <h1 className="text-2xl sm:text-3xl lg:text-3xl text-center font-extrabold">
              Confirmar Código
            </h1>
            <form onSubmit={isEmailSent ? handleConfirmation : handleSendCode} className="space-y-8 w-full max-w-lg mx-auto">
              {!isEmailSent ? (
                <>
                  <div className="flex flex-wrap -mx-8 mb-6">
                    <div className="w-full px-3 relative">
                      <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        className="py-4 px-10 text-base rounded-2xl border border-black focus:outline-none shadow-md transition duration-500 ease-in-out w-full"
                        placeholder="Digite seu e-mail"
                        required
                      />
                    </div>
                  </div>
                  <div className="text-center">
                    <button
                      type="submit"
                      className="mt-4 py-4 px-8 text-base rounded-full border-2 bg-slate-900 text-white font-semibold transition duration-1000 ease-in-out hover:bg-transparent hover:text-slate-900 hover:border-slate-900">
                      Enviar Código
                    </button>
                  </div>
                </>
              ) : (
                <>
                  <div className="flex flex-wrap -mx-8 mb-6">
                    <div className="w-full px-3 relative">
                      <input
                        type="text"
                        value={code}
                        onChange={(e) => setCode(e.target.value)}
                        className="py-4 px-10 text-base rounded-2xl border border-black focus:outline-none shadow-md transition duration-500 ease-in-out w-full"
                        placeholder="Digite o código de confirmação"
                        required
                      />
                    </div>
                  </div>
                  <div className="text-center">
                    <button
                      type="submit"
                      className="mt-4 py-4 px-8 text-base rounded-full border-2 bg-slate-900 text-white font-semibold transition duration-1000 ease-in-out hover:bg-transparent hover:text-slate-900 hover:border-slate-900">
                      Confirmar
                    </button>
                  </div>
                </>
              )}
            </form>
          </div>
        </div>
      </div>
    </>
  );
};

export default Confirmacao;
