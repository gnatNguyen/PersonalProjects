import time
from os import system
import os
import sys
from pynput.keyboard import Key, Controller as keyboard
from pynput.mouse import Button, Controller as mouse


k = keyboard()
m = mouse()

psych_words = "Basic Science.Behavior psychology.Behaviorism.Biological psychology.Biopsychosocial approach.case study.confounding variable.correlation.Correlational Research.Counseling psychology" \
              ".critical thinking .Cross-Sectional Studies.debriefing.dependent variable.descriptive statistics.Double-Blind Studies.Educational psychology.experiment.experimental group.hindsight bias" \
              ".Humanism.hypothesis .independent variable.informed consent.Longitudinal Studies.mean.median.mode.Nature-nurture issue.normal curve.observation.operational definition.placebo effect.population" \
              ".Positive psychology.Psychiatrist.Psychology.Psychometrics.Psychotherapist.random sample.range.replication.Samples (random & representative).sampling bias.scatterplot.Scientific Method" \
              ".skewed distribution.standard deviation.Structuralism.survey.Surveys (interviews & questionnaires).theory.Action potential.Adrenal glands.All-or-none response.Autonomic.Axon.Behavior genetics" \
              ".Biological psychology.Brain (amygdala, brainstem, hindbrain,pons, medulla, cerebellum, midbrain, forebrain, thalamus, reticular formation, hypothalamus).Broca’s Area/Werneike" \
              ".Central Nervous System.Cerebral Cortex .Chromosomes.Cognitive neuroscience.Corpus Callosum.Dendrites.DNA.EEG, PET, MRI, CT Scan.Endocrine System.Endorphins.Environment.Fissures" \
              ".Genetics.Glial cells.Gonads.Heritability.Hormones.Interneurons.Lesion.Limbic system.Lobes:  frontal, parietal, occipital, temporal.Motor (efferent) neurons.Motor cortex.Myelin sheath" \
              ".Neuron.Neurotransmitters.Pancreas.Parasympathetic nervous system.Peripheral Nervous System.Phenylketonuria (PKU).Pineal gland.Pituitary gland.Plasticity.Reuptake.Sensory (afferent) neurons" \
              ".Soma (cell body).Somatic nervous system.Split brain.Sympathetic nervous system.Synapse.Thyroid gland.Accommodation.Adolescence .Adulthood.Aggression.Assimilation.Attachment.Autonomy.Basic trust" \
              ".Conception.Concrete operational stage.Conservation.Critical period.Cross-sectional study.Dementia.Developmental norms.Developmental psychology.Egocentric.Embryo.Fetal alcohol syndrome.Fetus" \
              ".Habituation.Identity.Identity crisis.Imaginary audience.Imprinting.Innate reflexes.Intimacy.Maturation.Menarche.Menopause.Midlife crisis.Neonate.Object permanence.Parent-child relationship" \
              ".Peer group.Personal fable.Placenta.Puberty.Representational thought.Schema.Self-concept.Separation anxiety.Social clock.Strange anxiety.Temperament.Teratogens.chromosomes.Zygote.Absolute threshold" \
              ".Accommodation.Adaptation.Auditory Nerve.Binocular cues.Binocular fusion.Blind Spot.Bottom-up processing.Change blindness.Cochlea.Cochlear implant.Color constancy.Colorblindness.Cones.Decibel" \
              ".Depth perception.Difference Threshold.Figure-Ground .Fovea.Frequency theory.Gate-control theory.Gestalt principles of perceptual organization.Inattentional blindness.Intensity.Iris.Kinesthesia" \
              ".Lens.Monocular cues.Olfactory Nerve.Opponent Process Theory.Optic Nerve.Papillae.Parallel processing.Perception.Perceptual set.Perpetual adaptation.Phi phenomenon.Pitch .Place theory.Priming.Pupil" \
              ".Receptor Cells.Retina.Retinal disparity.Rods.Selective attention.Sensation.Sensory adaption.Top-down processing.Transduction .Vestibular Sense.Visual cliff.Visual Illusions" \
              ".Weber’s Law.Young-Helmholtz trichromatic theory.Addiction.Alcohol.Amphetamines.Barbiturates.Circadian cycle (rhythm).cocaine.Consciousness.Daydreaming.Depressants.Dissociation.Dreams" \
              ".Ecstasy.Hallucinogens.Hypnosis.Insomnia.Latent content.LSD.Meditation.methamphetamine.Narcolepsy.Nicotine.Night terrors.Nightmares.Opiates.Psychoactive drug.REM.REM rebound.Sleep apnea" \
              ".Sleep cycle.Stimulants.THC.Tolerance.Withdrawal.Acquisition.Aversion.Avoidance training.Behavior modification.Behaviorism.Chaining.Classical Conditioning.Cognitive learning.Cognitive map" \
              ".Continuous reinforcement.Discrimination.External locus of control.Extinction.Extrinsic motivation.Feedback.Generalization.Habituation.Internal locus of control.Intrinsic motivation.Latent learning" \
              ".Law of effect.Learned helplessness.Learning.Modeling.Neutral stimulus.Observational learning.Operant Conditioning.Pairing.Practice.Prosocial behavior .Punishment.Reinforcement.Reinforcers (positive and negative)" \
              ".Reinforcers (primary,secondary and token economy).Respondent behavior.Schedules of Reinforcement.Self-control.Shaping.Social Learning Theory.Spontaneous Recovery.Stimulus.Transfer.Aggression.Altruism" \
              ".Attribution theory.Bystander effect.cognitive dissonance therapy.Compliance.Conflict.Conformity.Culture.Deindividualism.Discrimination.Equity.Ethnicity.foot-in-the-door persuasion.frustration-aggression principle" \
              ".fundamental attribution error.Gender diversity.GRIT.Group decision making.group polarization.groupthink.Impression formation.informational social influence.Ingroup bias.Just-world phenomenon.Mere exposure effect" \
              ".Norm.normative social influence.Obedience.Other-race effect.Outgroup.Peripheral route persuasion.Prejudice.scapegoat theory.self-disclosure.Self-fulfilling prophecy.Social exchange theory.Social loafing.Social-responsibility norm" \
              ".Social psychology.Social trap.social facilitation.social loafing.Stereotype.Superordinate goal.Albert Bandura.BF Skinner.Carol Gilligan.Diana Baumrind.Edward Thorndike.Eleanor Gibson.Elizabeth Kobler Ross.Elizabeth Loftus" \
              ".Erik Erikson.Harry Harlow.Ivan Pavlov.Jean Piaget.John B. Watson.Konrad Lorenz.Lawrence Kohlberg.Martin Seligman.Mary Ainsworth.Mary Cover Jones.Philip Zimbardo.Sigmund Freud.Solomon Asch.Stanley Milgram.Wilhelm Wundt.William James"

time.sleep(1)
k.press(Key.cmd)
k.release(Key.cmd)
time.sleep(1.5)
k.type("Google")
time.sleep(.5)
k.press(Key.enter)
k.release(Key.enter)
time.sleep(5)
for x in psych_words:
    if x == ".":
        k.press(Key.enter)
        k.release(Key.enter)
        input()
        time.sleep(.5)
        k.press(Key.alt)
        k.press(Key.tab)
        k.release(Key.alt)
        k.release(Key.tab)
        time.sleep(1)
        k.press(Key.ctrl)
        k.press("k")
        k.release(Key.ctrl)
        k.release("k")
        time.sleep(1)
    else:
        k.type(x)



