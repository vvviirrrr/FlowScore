<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FlowScore | Professional Edition</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700;800&display=swap');
        
        body {
            font-family: 'Space Grotesk', sans-serif;
            background: #040408;
            color: #e2e8f0;
            height: 100vh;
            overflow: hidden;
            background-image: radial-gradient(circle at 0% 0%, #1a1a3a 0%, transparent 50%),
                              radial-gradient(circle at 100% 100%, #251a35 0%, transparent 50%);
        }

        .title-container {
            width: 100%;
            display: flex;
            justify-content: center;
            margin-bottom: 2rem;
        }

        .brand-title {
            background: linear-gradient(to right, #22d3ee, #818cf8, #f472b6, #22d3ee);
            background-size: 300% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientFlow 8s linear infinite;
            display: inline-block;
            white-space: nowrap;
            padding-right: 20px;
        }

        @keyframes gradientFlow {
            0% { background-position: 0% 50%; }
            100% { background-position: 300% 50%; }
        }

        .fixed-legend {
            position: fixed;
            top: 1.5rem;
            right: 2rem;
            z-index: 100;
            background: rgba(10, 10, 20, 0.9);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 0.8rem 1.2rem;
            border-radius: 1rem;
            width: 280px;
        }

        #cards-container {
            height: calc(100vh - 80px);
            overflow-y: auto;
            padding-top: 80px; 
            scrollbar-width: thin;
            scrollbar-color: #4f46e5 transparent;
        }

        .spectrum-card {
            background: rgba(25, 25, 45, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }

        .glow-risk { border-left: 4px solid #f43f5e; }
        .glow-mid { border-left: 4px solid #fbbf24; }
        .glow-prime { border-left: 4px solid #10b981; }

        .cyber-input {
            background: rgba(0, 0, 0, 0.6) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            color: #fff !important;
            padding: 0.85rem !important;
            font-size: 0.9rem;
        }

        .cyber-input:focus {
            border-color: #818cf8 !important;
            outline: none;
        }

        .hud-bar-container { display: flex; gap: 3px; height: 10px; width: 100%; }
        .hud-segment { flex: 1; height: 100%; border-radius: 1px; background: rgba(255, 255, 255, 0.03); }

        .card-content {
            display: grid;
            grid-template-rows: 0fr;
            transition: grid-template-rows 0.5s ease, opacity 0.3s ease;
            opacity: 0;
            overflow: hidden;
        }

        .card-expanded .card-content { grid-template-rows: 1fr; opacity: 1; }
        .card-expanded { background: rgba(35, 35, 55, 0.8) !important; padding-bottom: 1.5rem !important; }

        .advisor-box {
            background: rgba(99, 102, 241, 0.05);
            border: 1px solid rgba(99, 102, 241, 0.1);
            border-radius: 1.25rem;
        }
    </style>
</head>
<body class="p-4 lg:p-8">

    <div class="fixed-legend">
        <div class="flex justify-between text-[10px] font-black mb-2 tracking-widest text-slate-500">
            <span>POOR (300)</span>
            <span>PRIME (900)</span>
        </div>
        <div class="h-1.5 w-full rounded-full bg-gradient-to-r from-rose-500 via-amber-400 via-yellow-300 to-emerald-500"></div>
        <div class="flex justify-between text-[10px] font-bold mt-2 text-slate-400">
            <span>300</span>
            <span>450</span>
            <span>600</span>
            <span>750</span>
            <span>900</span>
        </div>
    </div>

    <div class="max-w-[1600px] mx-auto grid grid-cols-12 gap-10 h-full">
        
        <aside class="col-span-12 lg:col-span-4 flex flex-col">
            <div class="title-container">
                <h1 class="text-6xl font-extrabold tracking-tighter italic brand-title">FLOWSCORE</h1>
            </div>

            <div class="spectrum-card rounded-3xl p-8 border-t-2 border-t-indigo-500/20 shadow-2xl">
                <form id="assessment-form" class="space-y-6" autocomplete="off">
                    <div class="space-y-2">
                        <label class="text-[10px] font-bold text-slate-500 uppercase tracking-widest ml-1">Merchant Name</label>
                        <input type="text" id="vendor-name" placeholder="e.g. Acme Retail" class="cyber-input w-full rounded-xl" required>
                    </div>

                    <div class="grid grid-cols-2 gap-5">
                        <div class="space-y-2">
                            <label class="text-[10px] font-bold text-cyan-400 uppercase tracking-widest">Weekly Sales</label>
                            <input type="number" id="val-txns" placeholder="e.g. 50" class="cyber-input w-full rounded-xl" required>
                        </div>
                        <div class="space-y-2">
                            <label class="text-[10px] font-bold text-amber-400 uppercase tracking-widest">Unique Merchants</label>
                            <input type="number" id="val-merchants" placeholder="e.g. 12" class="cyber-input w-full rounded-xl" required>
                        </div>
                    </div>

                    <div class="grid grid-cols-2 gap-5">
                        <div class="space-y-2">
                            <label class="text-[10px] font-bold text-emerald-400 uppercase tracking-widest">Income Stability</label>
                            <input type="number" step="0.01" id="val-stability" placeholder="e.g. 0.85" class="cyber-input w-full rounded-xl" required>
                        </div>
                        <div class="space-y-2">
                            <label class="text-[10px] font-bold text-fuchsia-400 uppercase tracking-widest">Discipline</label>
                            <input type="number" step="0.01" id="val-discipline" placeholder="e.g. 0.90" class="cyber-input w-full rounded-xl" required>
                        </div>
                    </div>

                    <div class="space-y-2">
                        <label class="text-[10px] font-bold text-rose-400 uppercase tracking-widest">Savings</label>
                        <input type="number" step="0.01" id="val-savings" placeholder="e.g. 0.45" class="cyber-input w-full rounded-xl" required>
                    </div>

                    <button type="submit" class="w-full bg-gradient-to-r from-indigo-600 to-violet-700 hover:brightness-110 text-white font-bold py-4 rounded-xl transition-all shadow-lg active:scale-95 text-[10px] tracking-[0.3em] mt-2">
                        ANALYZE NOW
                    </button>
                </form>
            </div>
        </aside>

        <section class="col-span-12 lg:col-span-8" id="cards-container"></section>
    </div>

    <script>
        const form = document.getElementById('assessment-form');
        const container = document.getElementById('cards-container');

        form.onsubmit = (e) => {
            e.preventDefault();
            
            const name = document.getElementById('vendor-name').value;
            const txns = parseFloat(document.getElementById('val-txns').value);
            const merch = parseFloat(document.getElementById('val-merchants').value);
            const stab = parseFloat(document.getElementById('val-stability').value);
            const disc = parseFloat(document.getElementById('val-discipline').value);
            const sav = parseFloat(document.getElementById('val-savings').value);

            const nTxns = Math.min(txns / 100, 1);
            const nMerch = Math.min(merch / 20, 1);
            const score = Math.floor(300 + (((nTxns + nMerch + stab + disc + sav) / 5) * 600));
            
            // Logic updated to sync with Range Legend and Case brackets
            let glow = "glow-risk"; 
            if (score >= 750) {
                glow = "glow-prime"; // Emerald/Green (Elite)
            } else if (score >= 450) {
                glow = "glow-mid";   // Amber/Yellow (Emerging to Strong)
            }

            const card = document.createElement('div');
            card.className = `spectrum-card rounded-[1.25rem] cursor-pointer group mb-4 transition-all p-4 ${glow}`;
            
            card.innerHTML = `
                <div class="flex items-center justify-between" onclick="this.parentElement.classList.toggle('card-expanded')">
                    <div class="flex items-center gap-5">
                        <div class="h-10 w-10 bg-indigo-500/10 rounded-xl flex items-center justify-center text-indigo-300 font-bold border border-white/5">
                            ${name[0].toUpperCase()}
                        </div>
                        <div>
                            <h3 class="text-white font-bold text-lg leading-none">${name}</h3>
                            <p class="text-[9px] text-slate-500 font-bold uppercase tracking-widest mt-1">ID: FS-${Math.floor(Math.random()*9999)}</p>
                        </div>
                    </div>
                    <div class="flex items-center gap-8">
                        <div class="text-right">
                            <div class="text-3xl font-black text-white italic tracking-tighter">${score}</div>
                            <p class="text-[9px] font-bold text-slate-500 uppercase tracking-widest">Score</p>
                        </div>
                        <i class="fas fa-chevron-down text-slate-700 transition-colors"></i>
                    </div>
                </div>
                
                <div class="card-content">
                    <div class="min-h-0 pt-6 mt-6 border-t border-white/5">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                            <div class="grid grid-cols-1 gap-4">
                                ${createHUDBar("Weekly Sales", nTxns * 100, "#22d3ee")}
                                ${createHUDBar("Unique Merchants", nMerch * 100, "#fbbf24")}
                                ${createHUDBar("Income Stability", stab * 100, "#10b981")}
                                ${createHUDBar("Savings", sav * 100, "#f472b6")}
                            </div>
                            
                            <div class="advisor-box p-5 flex flex-col justify-between">
                                <div>
                                    <p class="text-[10px] font-bold text-indigo-400 uppercase tracking-widest mb-2">Strategic Recommendation</p>
                                    <p class="text-sm text-slate-300 leading-relaxed font-medium italic">
                                        "${getSimpleVerdict(score)}"
                                    </p>
                                </div>
                                <div class="mt-4 flex justify-between items-center opacity-30 text-[9px] font-bold uppercase">
                                    <span>Core_v5.1_Stable</span>
                                    <i class="fas fa-chart-line text-lg"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            `;

            container.prepend(card);
            form.reset();
        };

        // Detailed Bracketed Logic
        function getSimpleVerdict(s) {
            if (s < 450) {
                return "Critical volatility detected. Business shows inconsistent cash flow and insufficient reserves. Support is not recommended at this stage.";
            } else if (s >= 450 && s < 600) {
                return "Limited stability observed. While the business is operational, it lacks the volume for major expansion. Monitor closely for 30 days.";
            } else if (s >= 600 && s < 750) {
                return "Steady performance with healthy merchant diversity. This business is a safe candidate for standard credit and moderate growth support.";
            } else {
                return "Exceptional financial health and discipline. Business demonstrates high-tier stability and is ready for full-scale premium support.";
            }
        }

        function createHUDBar(label, pct, color) {
            let segments = '';
            for(let i=0; i<15; i++) {
                const active = (pct / 100) * 15 > i;
                segments += `<div class="hud-segment" style="background: ${active ? color : 'rgba(255,255,255,0.02)'}"></div>`;
            }
            return `
                <div>
                    <div class="flex justify-between text-[9px] font-bold text-slate-500 mb-1.5 uppercase tracking-widest">
                        <span>${label}</span>
                        <span style="color: ${color}">${Math.round(pct)}%</span>
                    </div>
                    <div class="hud-bar-container">${segments}</div>
                </div>
            `;
        }
    </script>
</body>
</html>