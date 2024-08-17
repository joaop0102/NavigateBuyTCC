import React, { useState, FormEvent } from 'react';
import Head from 'next/head';
import Link from 'next/link';
import { useRouter } from 'next/router';
import "../app/globals.css";

const EsqueciSenha: React.FC = () => {
    const [email, setEmail] = useState<string>('');
    const [message, setMessage] = useState<string>('');
    const [loading, setLoading] = useState<boolean>(false);
    const router = useRouter(); // Inicialização do useRouter

    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setLoading(true);

        try {
            const response = await fetch('http://localhost:5000/api/request-password-reset', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email }),
            });

            if (!response.ok) {
                throw new Error('Ocorreu um erro ao solicitar a redefinição de senha.');
            }

            setMessage('Email encontrado com sucesso!.');
            router.push('/redefinir_senha'); // Redireciona para a página desejada após sucesso
        } catch (error) {
            if (error instanceof Error) {
                setMessage(error.message || 'Ocorreu um erro.');
            } else {
                setMessage('Ocorreu um erro desconhecido.');
            }
        } finally {
            setLoading(false);
        }
    };

  return (
    <header className="flex flex-col md:flex-row h-screen">
      <Head>
        <title>Esqueceu a senha - Navigate Buy</title>
      </Head>
      <div className="flex-1 w-full h-full bg-white flex flex-col items-center justify-center">
        <div className="max-w-6xl mx-auto p-8">
          <h1 className="text-3xl sm:text-2xl md:text-2xl lg:text-3xl text-center font-extrabold">
            Esqueceu sua senha?
          </h1>
          <p className="text-xl sm:text-xl md:text-2xl lg:text-2xl text-center mb-8">
            Digite seu e-mail para receber instruções de redefinição.
          </p>
          <form className="space-y-10 w-full max-w-lg mx-auto" onSubmit={handleSubmit}>
            <div className="flex flex-wrap -mx-8 mb-6">
              <div className="w-full px-3 relative">
                <input
                  id="email"
                  type="email"
                  className="py-3 sm:py-4 md:py-5 lg:py-5 pl-12 sm:pl-14 md:pl-16 lg:pl-20 pr-4 w-full text-base sm:text-lg md:text-xl lg:text-2xl rounded-2xl border border-black focus:outline-none shadow-md transition duration-500 ease-in-out"
                  placeholder="Email"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>
            </div>
            <div className="text-center">
              <button
                type="submit"
                className={`mt-4 py-3 sm:py-4 md:py-5 lg:py-6 px-6 sm:px-8 md:px-16 lg:px-28 text-2xl sm:text-2xl md:text-2xl lg:text-2xl rounded-full border-2 ${loading ? 'bg-gray-500' : 'bg-slate-900'} text-white font-semibold transition duration-1000 ease-in-out hover:bg-white hover:text-slate-900 hover:border-slate-900`}
                disabled={loading}
              >
                {loading ? 'Enviando...' : 'Enviar Instruções'}
              </button>
              <Link href="/redefinir_senha" className="mt-4 block text-sm text-[#0E023B] hover:underline">
                Voltar ao Login
              </Link>
            </div>
            {message && (
              <div className="mt-4 text-center text-red-500">
                {message}
              </div>
            )}
          </form>
        </div>
      </div>
    </header>
  );
};

export default EsqueciSenha;
